from flask import Flask, request, redirect, url_for, render_template_string, abort
from datetime import datetime

app = Flask(__name__)

# "Base de datos" en memoria (solo para demo)
accounts = {}
next_id = 1


# ----------------------------
# Helpers
# ----------------------------
def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def parse_amount(value):
    try:
        amount = float(value)
        return amount
    except (TypeError, ValueError):
        return None

def get_account_or_404(account_id):
    acc = accounts.get(account_id)
    if not acc:
        abort(404)
    return acc

def add_tx(acc, kind, amount, note=""):
    acc["transactions"].append({
        "date": now_str(),
        "kind": kind,
        "amount": amount,
        "note": note
    })


# ----------------------------
# Templates (HTML simple)
# ----------------------------
INDEX_TPL = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mini Banco Flask</title>
</head>
<body>
    <h1>Mini Banco (Demo en Flask)</h1>

    {% if error %}
        <p style="color:red;"><b>Error:</b> {{ error }}</p>
    {% endif %}

    <h2>Crear cuenta</h2>
    <form action="{{ url_for('create_account') }}" method="post">
        <label>Nombre del titular:</label>
        <input type="text" name="owner" required>
        <br><br>
        <label>Depósito inicial (opcional):</label>
        <input type="number" step="0.01" min="0" name="initial">
        <br><br>
        <button type="submit">Crear</button>
    </form>

    <hr>

    <h2>Cuentas existentes</h2>
    {% if accounts %}
        <ul>
        {% for acc in accounts.values() %}
            <li>
                <b>ID {{ acc.id }}</b> — {{ acc.owner }} —
                Saldo: ${{ '%.2f'|format(acc.balance) }}
                [<a href="{{ url_for('view_account', account_id=acc.id) }}">Ver cuenta</a>]
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No hay cuentas todavía.</p>
    {% endif %}
</body>
</html>
"""

ACCOUNT_TPL = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Cuenta {{ acc.id }}</title>
</head>
<body>
    <a href="{{ url_for('index') }}">← Volver</a>
    <h1>Cuenta ID {{ acc.id }}</h1>
    <p><b>Titular:</b> {{ acc.owner }}</p>
    <p><b>Saldo actual:</b> ${{ '%.2f'|format(acc.balance) }}</p>

    <hr>

    <h2>Operaciones</h2>
    <ul>
        <li><a href="{{ url_for('deposit', account_id=acc.id) }}">Depositar</a></li>
        <li><a href="{{ url_for('withdraw', account_id=acc.id) }}">Retirar</a></li>
        <li><a href="{{ url_for('transfer', account_id=acc.id) }}">Transferir</a></li>
    </ul>

    <hr>

    <h2>Historial de transacciones</h2>
    {% if acc.transactions %}
        <table border="1" cellpadding="6">
            <tr>
                <th>Fecha</th>
                <th>Tipo</th>
                <th>Monto</th>
                <th>Nota</th>
            </tr>
            {% for tx in acc.transactions %}
            <tr>
                <td>{{ tx.date }}</td>
                <td>{{ tx.kind }}</td>
                <td>${{ '%.2f'|format(tx.amount) }}</td>
                <td>{{ tx.note }}</td>
            </tr>
            {% endfor %}
        </table>
    {% else %}
        <p>Sin movimientos todavía.</p>
    {% endif %}
</body>
</html>
"""

DEPOSIT_TPL = """
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Depósito</title></head>
<body>
    <a href="{{ url_for('view_account', account_id=acc.id) }}">← Volver a cuenta</a>
    <h1>Depositar a cuenta {{ acc.id }}</h1>

    {% if error %}
        <p style="color:red;"><b>Error:</b> {{ error }}</p>
    {% endif %}

    <form method="post">
        <label>Monto a depositar:</label>
        <input type="number" step="0.01" min="0.01" name="monto" required>
        <button type="submit">Depositar</button>
    </form>
</body>
</html>
"""

WITHDRAW_TPL = """
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Retiro</title></head>
<body>
    <a href="{{ url_for('view_account', account_id=acc.id) }}">← Volver a cuenta</a>
    <h1>Retirar de cuenta {{ acc.id }}</h1>

    <p>Saldo disponible: ${{ '%.2f'|format(acc.balance) }}</p>

    {% if error %}
        <p style="color:red;"><b>Error:</b> {{ error }}</p>
    {% endif %}

    <form method="post">
        <label>Monto a retirar:</label>
        <input type="number" step="0.01" min="0.01" name="monto" required>
        <button type="submit">Retirar</button>
    </form>
</body>
</html>
"""

TRANSFER_TPL = """
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Transferencia</title></head>
<body>
    <a href="{{ url_for('view_account', account_id=acc.id) }}">← Volver a cuenta</a>
    <h1>Transferir desde cuenta {{ acc.id }}</h1>

    <p>Saldo disponible: ${{ '%.2f'|format(acc.balance) }}</p>

    {% if error %}
        <p style="color:red;"><b>Error:</b> {{ error }}</p>
    {% endif %}

    {% if destinations %}
    <form method="post">
        <label>Cuenta destino:</label>
        <select name="destino" required>
            {% for d in destinations %}
                <option value="{{ d.id }}">ID {{ d.id }} — {{ d.owner }}</option>
            {% endfor %}
        </select>
        <br><br>
        <label>Monto a transferir:</label>
        <input type="number" step="0.01" min="0.01" name="monto" required>
        <br><br>
        <button type="submit">Transferir</button>
    </form>
    {% else %}
        <p>No hay otras cuentas para transferir.</p>
    {% endif %}
</body>
</html>
"""


# ----------------------------
# Rutas
# ----------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template_string(INDEX_TPL, accounts=accounts, error=None)


@app.route("/crear", methods=["POST"])
def create_account():
    global next_id

    owner = (request.form.get("owner") or "").strip()
    initial = parse_amount(request.form.get("initial"))

    if not owner:
        return render_template_string(INDEX_TPL, accounts=accounts, error="El nombre del titular es obligatorio.")

    if initial is None:
        initial = 0.0
    if initial < 0:
        return render_template_string(INDEX_TPL, accounts=accounts, error="El depósito inicial no puede ser negativo.")

    acc_id = next_id
    next_id += 1

    accounts[acc_id] = {
        "id": acc_id,
        "owner": owner,
        "balance": initial,
        "transactions": []
    }

    if initial > 0:
        add_tx(accounts[acc_id], "Apertura", initial, "Depósito inicial")

    return redirect(url_for("view_account", account_id=acc_id))


@app.route("/cuenta/<int:account_id>", methods=["GET"])
def view_account(account_id):
    acc = get_account_or_404(account_id)
    return render_template_string(ACCOUNT_TPL, acc=acc)


@app.route("/deposito/<int:account_id>", methods=["GET", "POST"])
def deposit(account_id):
    acc = get_account_or_404(account_id)
    error = None

    if request.method == "POST":
        amount = parse_amount(request.form.get("monto"))
        if amount is None or amount <= 0:
            error = "Monto inválido."
        else:
            acc["balance"] += amount
            add_tx(acc, "Depósito", amount)
            return redirect(url_for("view_account", account_id=account_id))

    return render_template_string(DEPOSIT_TPL, acc=acc, error=error)


@app.route("/retiro/<int:account_id>", methods=["GET", "POST"])
def withdraw(account_id):
    acc = get_account_or_404(account_id)
    error = None

    if request.method == "POST":
        amount = parse_amount(request.form.get("monto"))
        if amount is None or amount <= 0:
            error = "Monto inválido."
        elif amount > acc["balance"]:
            error = "Fondos insuficientes."
        else:
            acc["balance"] -= amount
            add_tx(acc, "Retiro", amount)
            return redirect(url_for("view_account", account_id=account_id))

    return render_template_string(WITHDRAW_TPL, acc=acc, error=error)


@app.route("/transferencia/<int:account_id>", methods=["GET", "POST"])
def transfer(account_id):
    acc = get_account_or_404(account_id)
    error = None

    destinations = [a for a in accounts.values() if a["id"] != account_id]

    if request.method == "POST":
        dest_id = request.form.get("destino")
        amount = parse_amount(request.form.get("monto"))

        if not dest_id:
            error = "Seleccione cuenta destino."
        else:
            try:
                dest_id = int(dest_id)
            except ValueError:
                dest_id = None

        dest_acc = accounts.get(dest_id) if dest_id else None

        if error is None:
            if not dest_acc:
                error = "La cuenta destino no existe."
            elif amount is None or amount <= 0:
                error = "Monto inválido."
            elif amount > acc["balance"]:
                error = "Fondos insuficientes."
            else:
                # Movimiento
                acc["balance"] -= amount
                dest_acc["balance"] += amount

                add_tx(acc, "Transferencia enviada", amount, f"A cuenta ID {dest_acc['id']}")
                add_tx(dest_acc, "Transferencia recibida", amount, f"De cuenta ID {acc['id']}")

                return redirect(url_for("view_account", account_id=account_id))

    return render_template_string(TRANSFER_TPL, acc=acc, destinations=destinations, error=error)


if __name__ == "__main__":
    app.run(debug=True)
