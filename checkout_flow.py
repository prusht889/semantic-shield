from payment_gateway import process_credit_card

def submit_user_cart(cart_id: str):
    """Triggers the final payment transaction sequence on checkout submission."""
    print(f"🛒 [Checkout] Submitting cart: {cart_id}")
    process_credit_card("TOKEN_SECRET_XYZ_12345", 150.00)
