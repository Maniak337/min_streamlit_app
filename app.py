import streamlit as st

if 'balance' not in st.session_state:
    st.session_state.balance = 0
def show_balance():
    st.write(f"Ditt nuvarande saldo är: {st.session_state.balance} kr")

def deposit(amount):
    st.session_state.balance += amount
    st.write(f"Du har satt in {amount} kr.")

def buy_ticket(price):
    if st.session_state.balance >= price:
        st.session_state.balance -= price
        st.write(f"Du har köpt en biljett för {price} kr.")
    else:
        st.write("Du har inte tillräckligt med pengar på kontot för att köpa biljetten.")

st.title("Tågbiljett Kalkylator med Bank Konto")
st.header("Nuvarande Saldo")
show_balance()

st.header("Lägg in Pengar")
amount = st.number_input("Ange belopp att sätta in:", min_value=0, step=10)
if st.button("Lägg In"):
    deposit(amount)
    show_balance()

st.header("Köp Biljett")
ticket_price = st.number_input("Skriv biljettpris:", min_value=0, step=10)
if st.button("Köp Biljett"):
    buy_ticket(ticket_price)
    show_balance()
