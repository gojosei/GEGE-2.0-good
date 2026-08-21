import streamlit as st
import random
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

# ============================================================
# GEGE TRADING
# Complete Paper-Trading / Demo Simulator
# ============================================================

st.set_page_config(
    page_title="GEGE Trading",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background: #080d1a;
        color: #ffffff;
    }

    header {
        background: #080d1a !important;
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 3rem;
        max-width: 1600px;
    }

    .gege-logo {
        font-size: 44px;
        font-weight: 900;
        letter-spacing: 5px;
        color: #00e5ff;
        line-height: 1;
    }

    .subtitle {
        color: #8390ad;
        font-size: 14px;
        margin-top: 6px;
    }

    .demo-badge {
        display: inline-block;
        background: rgba(0, 230, 118, 0.10);
        color: #00e676;
        border: 1px solid rgba(0, 230, 118, 0.35);
        border-radius: 20px;
        padding: 5px 12px;
        font-size: 12px;
        font-weight: 700;
    }

    .dashboard-card {
        background: linear-gradient(145deg, #111a30, #0d1528);
        border: 1px solid #24304c;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 12px;
    }

    .card-label {
        color: #8390ad;
        font-size: 13px;
        margin-bottom: 7px;
    }

    .card-value {
        color: #ffffff;
        font-size: 27px;
        font-weight: 800;
    }

    .green {
        color: #00e676;
    }

    .red {
        color: #ff5252;
    }

    .cyan {
        color: #00e5ff;
    }

    .trade-panel {
        background: linear-gradient(145deg, #121b31, #0e1629);
        border: 1px solid #263453;
        border-radius: 18px;
        padding: 22px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .asset-price {
        color: #ffffff;
        font-size: 36px;
        font-weight: 900;
    }

    .small-muted {
        color: #71809d;
        font-size: 12px;
    }

    .stButton > button {
        width: 100%;
        min-height: 45px;
        border-radius: 9px;
        font-weight: 800;
        border: 1px solid #2b3858;
    }

    div[data-testid="stMetric"] {
        background: #111a30;
        border: 1px solid #26304d;
        padding: 15px;
        border-radius: 14px;
    }

    div[data-baseweb="select"] > div {
        background-color: #111a30;
    }

    .positive {
        color: #00e676;
        font-weight: 800;
    }

    .negative {
        color: #ff5252;
        font-weight: 800;
    }

    .sidebar-title {
        color: #00e5ff;
        font-size: 25px;
        font-weight: 900;
        letter-spacing: 3px;
    }

    /* ========================================================
       GEGE TUTORIAL ANIMATION
       ======================================================== */
    .tutorial-wrap {
        background: linear-gradient(135deg, #101a31 0%, #0b1223 55%, #111a30 100%);
        border: 1px solid #2b3b60;
        border-radius: 20px;
        padding: 24px;
        margin: 8px 0 24px 0;
        overflow: hidden;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25);
        animation: tutorialFade 0.7s ease-out;
    }

    .tutorial-title {
        font-size: 26px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 4px;
    }

    .tutorial-subtitle {
        color: #8390ad;
        font-size: 13px;
        margin-bottom: 18px;
    }

    .tutorial-track {
        display: flex;
        gap: 12px;
        width: max-content;
        animation: tutorialSlide 16s ease-in-out infinite;
    }

    .tutorial-step {
        width: 190px;
        min-height: 105px;
        background: rgba(17, 26, 48, 0.95);
        border: 1px solid #263453;
        border-radius: 14px;
        padding: 15px;
        box-sizing: border-box;
    }

    .tutorial-number {
        display: inline-flex;
        width: 28px;
        height: 28px;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: #00e5ff;
        color: #07101d;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .tutorial-step-title {
        color: #ffffff;
        font-weight: 800;
        font-size: 14px;
    }

    .tutorial-step-text {
        color: #8390ad;
        font-size: 11px;
        margin-top: 4px;
        line-height: 1.4;
    }

    .tutorial-pulse {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: #00e676;
        border-radius: 50%;
        margin-right: 6px;
        animation: tutorialPulse 1.2s infinite;
    }

    @keyframes tutorialFade {
        from { opacity: 0; transform: translateY(-12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes tutorialPulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.7); opacity: 0.55; }
    }

    @keyframes tutorialSlide {
        0%, 12% { transform: translateX(0); }
        18%, 30% { transform: translateX(-202px); }
        36%, 48% { transform: translateX(-404px); }
        54%, 66% { transform: translateX(-606px); }
        72%, 84% { transform: translateX(-808px); }
        90%, 100% { transform: translateX(0); }
    }

    @media (max-width: 800px) {
        .tutorial-step { width: 160px; }
        .tutorial-title { font-size: 21px; }
    }

    hr {
        border-color: #202c46;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ASSETS
# ============================================================

ASSETS = {
    "BTC": {
        "name": "Bitcoin",
        "symbol": "₿",
        "price": 67420.00,
        "volatility": 450,
    },
    "ETH": {
        "name": "Ethereum",
        "symbol": "Ξ",
        "price": 3450.00,
        "volatility": 35,
    },
    "SOL": {
        "name": "Solana",
        "symbol": "◎",
        "price": 182.00,
        "volatility": 4,
    },
    "XRP": {
        "name": "XRP",
        "symbol": "✕",
        "price": 0.61,
        "volatility": 0.025,
    },
    "ADA": {
        "name": "Cardano",
        "symbol": "₳",
        "price": 0.42,
        "volatility": 0.02,
    },
}


# ============================================================
# SESSION STATE
# ============================================================

def initialize_state():
    if "balance" not in st.session_state:
        st.session_state.balance = 10000.00

    if "selected_asset" not in st.session_state:
        st.session_state.selected_asset = "BTC"

    if "holdings" not in st.session_state:
        st.session_state.holdings = {
            asset: 0.0 for asset in ASSETS
        }

    if "prices" not in st.session_state:
        st.session_state.prices = {}

        for asset, data in ASSETS.items():
            base = data["price"]

            st.session_state.prices[asset] = [
                base * random.uniform(0.96, 1.04)
                for _ in range(80)
            ]

    if "transactions" not in st.session_state:
        st.session_state.transactions = []

    if "watchlist" not in st.session_state:
        st.session_state.watchlist = [
            "BTC",
            "ETH",
            "SOL",
        ]

    if "limit_orders" not in st.session_state:
        st.session_state.limit_orders = []

    if "starting_balance" not in st.session_state:
        st.session_state.starting_balance = 10000.00


initialize_state()

# Tutorial state
if "show_tutorial" not in st.session_state:
    st.session_state.show_tutorial = True


# ============================================================
# PRICE ENGINE
# ============================================================

def update_prices():
    for asset, data in ASSETS.items():

        old_price = st.session_state.prices[asset][-1]

        movement = random.uniform(
            -data["volatility"],
            data["volatility"],
        )

        new_price = old_price + movement

        minimum = 0.0001

        if new_price < minimum:
            new_price = minimum

        st.session_state.prices[asset].append(new_price)

        if len(st.session_state.prices[asset]) > 100:
            st.session_state.prices[asset].pop(0)


update_prices()


# ============================================================
# HELPERS
# ============================================================

def get_price(asset):
    return st.session_state.prices[asset][-1]


def get_previous_price(asset):
    prices = st.session_state.prices[asset]

    if len(prices) < 2:
        return prices[-1]

    return prices[-2]


def format_price(price):
    if price >= 1000:
        return f"${price:,.2f}"

    if price >= 1:
        return f"${price:,.4f}"

    return f"${price:,.6f}"


def calculate_portfolio_value():
    value = st.session_state.balance

    for asset in ASSETS:
        value += (
            st.session_state.holdings[asset]
            * get_price(asset)
        )

    return value


def calculate_asset_value(asset):
    return (
        st.session_state.holdings[asset]
        * get_price(asset)
    )


def add_transaction(
    transaction_type,
    asset,
    amount,
    price,
    value,
):
    st.session_state.transactions.append(
        {
            "Time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "Type": transaction_type,
            "Asset": asset,
            "Amount": amount,
            "Price": price,
            "Value": value,
        }
    )


def execute_buy(asset, amount):
    price = get_price(asset)
    cost = amount * price

    if amount <= 0:
        return False, "Amount must be greater than zero."

    if cost > st.session_state.balance:
        return False, "Insufficient demo balance."

    st.session_state.balance -= cost
    st.session_state.holdings[asset] += amount

    add_transaction(
        "BUY",
        asset,
        amount,
        price,
        cost,
    )

    return True, f"Bought {amount:.6f} {asset}"


def execute_sell(asset, amount):
    price = get_price(asset)

    if amount <= 0:
        return False, "Amount must be greater than zero."

    if amount > st.session_state.holdings[asset]:
        return False, f"Insufficient {asset} holdings."

    value = amount * price

    st.session_state.holdings[asset] -= amount
    st.session_state.balance += value

    add_transaction(
        "SELL",
        asset,
        amount,
        price,
        value,
    )

    return True, f"Sold {amount:.6f} {asset}"


def reset_account():
    st.session_state.balance = 10000.00

    st.session_state.holdings = {
        asset: 0.0 for asset in ASSETS
    }

    st.session_state.transactions = []
    st.session_state.limit_orders = []


# ============================================================
# CHECK LIMIT ORDERS
# ============================================================

def process_limit_orders():

    if not st.session_state.limit_orders:
        return

    remaining_orders = []

    for order in st.session_state.limit_orders:

        asset = order["Asset"]
        order_type = order["Type"]
        amount = order["Amount"]
        target = order["Target Price"]

        current = get_price(asset)

        triggered = False

        if order_type == "BUY":
            if current <= target:
                triggered = True

        elif order_type == "SELL":
            if current >= target:
                triggered = True

        if triggered:

            if order_type == "BUY":

                success, _ = execute_buy(
                    asset,
                    amount,
                )

                if not success:
                    remaining_orders.append(order)

            else:

                success, _ = execute_sell(
                    asset,
                    amount,
                )

                if not success:
                    remaining_orders.append(order)

        else:
            remaining_orders.append(order)

    st.session_state.limit_orders = remaining_orders


process_limit_orders()


# ============================================================
# CURRENT VALUES
# ============================================================

selected_asset = st.session_state.selected_asset
current_price = get_price(selected_asset)
previous_price = get_previous_price(selected_asset)

price_change = current_price - previous_price

if previous_price != 0:
    price_change_pct = (
        price_change / previous_price
    ) * 100
else:
    price_change_pct = 0

portfolio_value = calculate_portfolio_value()

total_pnl = (
    portfolio_value
    - st.session_state.starting_balance
)

total_pnl_pct = (
    total_pnl
    / st.session_state.starting_balance
) * 100


# ============================================================
# HEADER
# ============================================================

header_col1, header_col2 = st.columns(
    [3, 1]
)

with header_col1:

    st.markdown(
        '<div class="gege-logo">GEGE</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="subtitle">'
        'Professional Paper Trading Dashboard'
        '</div>',
        unsafe_allow_html=True,
    )

with header_col2:

    st.markdown(
        '<div style="text-align:right;">'
        '<span class="demo-badge">'
        '● PAPER TRADING'
        '</span>'
        '</div>',
        unsafe_allow_html=True,
    )

st.divider()

# ============================================================
# INTERACTIVE TUTORIAL
# ============================================================

if st.session_state.show_tutorial:
    tutorial_col, close_col = st.columns([6, 1])

    with tutorial_col:
        st.markdown(
            '''
            <div class="tutorial-wrap">
                <div class="tutorial-title">
                    🎓 How to use GEGE
                </div>
                <div class="tutorial-subtitle">
                    <span class="tutorial-pulse"></span>
                    Quick paper-trading walkthrough • Demo mode only
                </div>

                <div style="overflow:hidden;">
                    <div class="tutorial-track">
                        <div class="tutorial-step">
                            <div class="tutorial-number">1</div>
                            <div class="tutorial-step-title">Choose an asset</div>
                            <div class="tutorial-step-text">
                                Pick BTC, ETH, SOL, XRP or ADA from the market selector.
                            </div>
                        </div>

                        <div class="tutorial-step">
                            <div class="tutorial-number">2</div>
                            <div class="tutorial-step-title">Read the chart</div>
                            <div class="tutorial-step-text">
                                Watch the simulated price movement and review the trend.
                            </div>
                        </div>

                        <div class="tutorial-step">
                            <div class="tutorial-number">3</div>
                            <div class="tutorial-step-title">Set your amount</div>
                            <div class="tutorial-step-text">
                                Enter how much of the selected demo asset you want to trade.
                            </div>
                        </div>

                        <div class="tutorial-step">
                            <div class="tutorial-number">4</div>
                            <div class="tutorial-step-title">BUY or SELL</div>
                            <div class="tutorial-step-text">
                                Use the green BUY or red SELL button to place a demo trade.
                            </div>
                        </div>

                        <div class="tutorial-step">
                            <div class="tutorial-number">5</div>
                            <div class="tutorial-step-title">Monitor</div>
                            <div class="tutorial-step-text">
                                Track your cash, holdings, portfolio value and P&amp;L.
                            </div>
                        </div>

                        <div class="tutorial-step">
                            <div class="tutorial-number">6</div>
                            <div class="tutorial-step-title">Review</div>
                            <div class="tutorial-step-text">
                                Check your portfolio and transaction history after trading.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            ''',
            unsafe_allow_html=True,
        )

    with close_col:
        if st.button("✕ Close", use_container_width=True):
            st.session_state.show_tutorial = False
            st.rerun()
else:
    if st.button("🎓 Show Tutorial", use_container_width=False):
        st.session_state.show_tutorial = True
        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">⚡ GEGE</div>',
        unsafe_allow_html=True,
    )

    st.caption("Trading Simulator")

    st.divider()

    st.markdown("### 💰 Account")

    st.metric(
        "Cash",
        f"${st.session_state.balance:,.2f}",
    )

    st.metric(
        "Portfolio",
        f"${portfolio_value:,.2f}",
    )

    if total_pnl >= 0:

        st.metric(
            "Total P&L",
            f"+${total_pnl:,.2f}",
            f"+{total_pnl_pct:.2f}%",
        )

    else:

        st.metric(
            "Total P&L",
            f"-${abs(total_pnl):,.2f}",
            f"{total_pnl_pct:.2f}%",
        )

    st.divider()

    st.markdown("### 📊 Market")

    selected = st.selectbox(
        "Select Asset",
        list(ASSETS.keys()),
        index=list(ASSETS.keys()).index(
            st.session_state.selected_asset
        ),
    )

    if selected != st.session_state.selected_asset:
        st.session_state.selected_asset = selected
        st.rerun()

    st.write(
        f"**{ASSETS[selected]['name']}**"
    )

    st.write(
        f"Current: **{format_price(get_price(selected))}**"
    )

    st.divider()

    st.markdown("### ⭐ Watchlist")

    for asset in st.session_state.watchlist:

        price = get_price(asset)
        old = get_previous_price(asset)

        change = (
            ((price - old) / old) * 100
            if old
            else 0
        )

        color = "#00e676" if change >= 0 else "#ff5252"

        st.markdown(
            f"""
            <div style="
                padding:8px 0;
                border-bottom:1px solid #202c46;
            ">
                <b>{ASSETS[asset]['symbol']} {asset}</b>
                <span style="float:right;">
                    {format_price(price)}
                </span>
                <br>
                <small style="
                    color:{color};
                ">
                    {change:+.2f}%
                </small>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.info(
        "Demo environment only. "
        "No real money is involved."
    )

    if st.button("🎓 Tutorial", use_container_width=True):
        st.session_state.show_tutorial = True
        st.rerun()


# ============================================================
# TOP METRICS
# ============================================================

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.metric(
        f"{ASSETS[selected_asset]['symbol']} "
        f"{selected_asset}/USD",
        format_price(current_price),
        f"{price_change_pct:+.2f}%",
    )

with metric2:

    st.metric(
        "Cash Balance",
        f"${st.session_state.balance:,.2f}",
    )

with metric3:

    st.metric(
        "Portfolio Value",
        f"${portfolio_value:,.2f}",
    )

with metric4:

    if total_pnl >= 0:
        st.metric(
            "P&L",
            f"+${total_pnl:,.2f}",
            f"+{total_pnl_pct:.2f}%",
        )
    else:
        st.metric(
            "P&L",
            f"-${abs(total_pnl):,.2f}",
            f"{total_pnl_pct:.2f}%",
        )


st.write("")


# ============================================================
# MAIN DASHBOARD
# ============================================================

chart_col, trade_col = st.columns(
    [2.2, 1]
)


# ============================================================
# CHART
# ============================================================

with chart_col:

    title_col, selector_col = st.columns(
        [3, 1]
    )

    with title_col:

        st.markdown(
            f'<div class="section-title">'
            f'{ASSETS[selected_asset]["symbol"]} '
            f'{selected_asset}/USD'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<span class="demo-badge">'
            '● LIVE DEMO'
            '</span>',
            unsafe_allow_html=True,
        )

    with selector_col:

        chart_type = st.selectbox(
            "Chart",
            [
                "Line",
                "Area",
            ],
            label_visibility="collapsed",
        )

    st.write("")

    chart_prices = st.session_state.prices[
        selected_asset
    ]

    if chart_type == "Line":

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                y=chart_prices,
                mode="lines",
                line=dict(
                    color="#00e5ff",
                    width=3,
                ),
                fill=None,
            )
        )

    else:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                y=chart_prices,
                mode="lines",
                line=dict(
                    color="#00e5ff",
                    width=2,
                ),
                fill="tozeroy",
                fillcolor="rgba(0,229,255,0.10)",
            )
        )

    fig.update_layout(
        height=440,
        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10,
        ),
        paper_bgcolor="#111a30",
        plot_bgcolor="#111a30",
        font=dict(
            color="#8390ad",
        ),
        xaxis=dict(
            showgrid=False,
            showticklabels=False,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="#202c46",
            tickprefix="$",
        ),
        hovermode="x unified",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.caption(
        "Simulated market price movement."
    )


# ============================================================
# TRADE PANEL
# ============================================================

with trade_col:

    st.markdown(
        '<div class="trade-panel">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">'
        'Trade'
        '</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown(
        f'<div class="asset-price">'
        f'{format_price(current_price)}'
        f'</div>',
        unsafe_allow_html=True,
    )

    change_color = (
        "#00e676"
        if price_change >= 0
        else "#ff5252"
    )

    st.markdown(
        f'<div style="color:{change_color};">'
        f'{price_change:+,.4f} '
        f'({price_change_pct:+.2f}%)'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    order_type = st.radio(
        "Order Type",
        [
            "Market",
            "Limit",
        ],
        horizontal=True,
    )

    amount = st.number_input(
        f"Amount ({selected_asset})",
        min_value=0.000001,
        value=0.01,
        step=0.01,
        format="%.6f",
    )

    if order_type == "Limit":

        limit_price = st.number_input(
            "Limit Price",
            min_value=0.000001,
            value=float(current_price),
            step=max(
                current_price * 0.01,
                0.000001,
            ),
            format="%.6f",
        )

        estimated_value = (
            amount * limit_price
        )

    else:

        limit_price = None

        estimated_value = (
            amount * current_price
        )

    st.info(
        f"Estimated value: "
        f"**{format_price(estimated_value)}**"
    )

    buy_col, sell_col = st.columns(2)

    # --------------------------------------------------------
    # BUY
    # --------------------------------------------------------

    with buy_col:

        if st.button(
            "🟢 BUY",
            use_container_width=True,
        ):

            if order_type == "Market":

                success, message = execute_buy(
                    selected_asset,
                    amount,
                )

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

            else:

                order = {
                    "Time": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    "Type": "BUY",
                    "Asset": selected_asset,
                    "Amount": amount,
                    "Target Price": limit_price,
                }

                st.session_state.limit_orders.append(
                    order
                )

                st.success(
                    f"Limit BUY created at "
                    f"{format_price(limit_price)}"
                )

    # --------------------------------------------------------
    # SELL
    # --------------------------------------------------------

    with sell_col:

        if st.button(
            "🔴 SELL",
            use_container_width=True,
        ):

            if order_type == "Market":

                success, message = execute_sell(
                    selected_asset,
                    amount,
                )

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

            else:

                if amount > st.session_state.holdings[
                    selected_asset
                ]:

                    st.error(
                        "You don't have enough "
                        f"{selected_asset}."
                    )

                else:

                    order = {
                        "Time": datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                        "Type": "SELL",
                        "Asset": selected_asset,
                        "Amount": amount,
                        "Target Price": limit_price,
                    }

                    st.session_state.limit_orders.append(
                        order
                    )

                    st.success(
                        f"Limit SELL created at "
                        f"{format_price(limit_price)}"
                    )

    st.write("")

    owned = st.session_state.holdings[
        selected_asset
    ]

    st.caption(
        f"You own: {owned:.6f} {selected_asset}"
    )

    st.caption(
        f"Available cash: "
        f"${st.session_state.balance:,.2f}"
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


# ============================================================
# PORTFOLIO
# ============================================================

st.write("")
st.divider()

st.markdown(
    '<div class="section-title">'
    '💼 Portfolio'
    '</div>',
    unsafe_allow_html=True,
)

st.write("")

portfolio_rows = []

for asset in ASSETS:

    quantity = st.session_state.holdings[asset]

    price = get_price(asset)

    value = quantity * price

    allocation = (
        value / portfolio_value * 100
        if portfolio_value > 0
        else 0
    )

    portfolio_rows.append(
        {
            "Asset": asset,
            "Name": ASSETS[asset]["name"],
            "Holdings": quantity,
            "Price": price,
            "Value": value,
            "Allocation": allocation,
        }
    )

portfolio_df = pd.DataFrame(
    portfolio_rows
)

portfolio_display = portfolio_df.copy()

portfolio_display["Holdings"] = (
    portfolio_display["Holdings"]
    .map(lambda x: f"{x:.6f}")
)

portfolio_display["Price"] = (
    portfolio_display["Price"]
    .map(format_price)
)

portfolio_display["Value"] = (
    portfolio_display["Value"]
    .map(lambda x: f"${x:,.2f}")
)

portfolio_display["Allocation"] = (
    portfolio_display["Allocation"]
    .map(lambda x: f"{x:.2f}%")
)

st.dataframe(
    portfolio_display,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# PORTFOLIO METRICS
# ============================================================

p1, p2, p3 = st.columns(3)

with p1:

    st.metric(
        "Cash Balance",
        f"${st.session_state.balance:,.2f}",
    )

with p2:

    crypto_value = (
        portfolio_value
        - st.session_state.balance
    )

    st.metric(
        "Crypto Value",
        f"${crypto_value:,.2f}",
    )

with p3:

    st.metric(
        "Total Portfolio",
        f"${portfolio_value:,.2f}",
    )


# ============================================================
# OPEN LIMIT ORDERS
# ============================================================

st.write("")
st.divider()

st.markdown(
    '<div class="section-title">'
    '📌 Open Limit Orders'
    '</div>',
    unsafe_allow_html=True,
)

if st.session_state.limit_orders:

    orders_df = pd.DataFrame(
        st.session_state.limit_orders
    )

    st.dataframe(
        orders_df,
        use_container_width=True,
        hide_index=True,
    )

    if st.button(
        "Cancel All Limit Orders"
    ):

        st.session_state.limit_orders = []

        st.success(
            "All limit orders cancelled."
        )

        st.rerun()

else:

    st.info(
        "No open limit orders."
    )


# ============================================================
# TRANSACTION HISTORY
# ============================================================

st.write("")
st.divider()

st.markdown(
    '<div class="section-title">'
    '📋 Transaction History'
    '</div>',
    unsafe_allow_html=True,
)

if st.session_state.transactions:

    transactions = list(
        reversed(
            st.session_state.transactions
        )
    )

    transaction_df = pd.DataFrame(
        transactions
    )

    transaction_df["Amount"] = (
        transaction_df["Amount"]
        .map(lambda x: f"{x:.6f}")
    )

    transaction_df["Price"] = (
        transaction_df["Price"]
        .map(format_price)
    )

    transaction_df["Value"] = (
        transaction_df["Value"]
        .map(lambda x: f"${x:,.2f}")
    )

    st.dataframe(
        transaction_df,
        use_container_width=True,
        hide_index=True,
    )

else:

    st.info(
        "No trades yet. "
        "Your transactions will appear here."
    )


# ============================================================
# MARKET OVERVIEW
# ============================================================

st.write("")
st.divider()

st.markdown(
    '<div class="section-title">'
    '🌐 Market Overview'
    '</div>',
    unsafe_allow_html=True,
)

market_cols = st.columns(
    len(ASSETS)
)

for index, asset in enumerate(ASSETS):

    price = get_price(asset)
    old = get_previous_price(asset)

    change = (
        ((price - old) / old) * 100
        if old
        else 0
    )

    with market_cols[index]:

        st.markdown(
            '<div class="dashboard-card">',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="card-label">'
            f'{ASSETS[asset]["symbol"]} '
            f'{asset}'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="card-value">'
            f'{format_price(price)}'
            f'</div>',
            unsafe_allow_html=True,
        )

        color_class = (
            "green"
            if change >= 0
            else "red"
        )

        st.markdown(
            f'<div class="{color_class}">'
            f'{change:+.2f}%'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True,
        )


# ============================================================
# ACCOUNT CONTROLS
# ============================================================

st.write("")
st.divider()

st.markdown(
    '<div class="section-title">'
    '⚙️ Account Controls'
    '</div>',
    unsafe_allow_html=True,
)

st.write("")

reset_col, refresh_col = st.columns(2)

with reset_col:

    if st.button(
        "🔄 Reset Demo Account",
        use_container_width=True,
    ):

        reset_account()

        st.success(
            "Demo account reset to $10,000."
        )

        st.rerun()

with refresh_col:

    if st.button(
        "🔃 Refresh Market",
        use_container_width=True,
    ):

        update_prices()

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.write("")
st.write("")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#596781;
        padding:25px;
        border-top:1px solid #202c46;
    ">
        <strong style="color:#00e5ff;">
            GEGE TRADING
        </strong>
        <br>
        Paper Trading Simulator
        <br>
        <small>
            Simulated prices and trades only •
            No real money is involved
        </small>
    </div>
    """,
    unsafe_allow_html=True,
)