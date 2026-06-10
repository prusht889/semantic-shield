from auth_service import validate_vault_token

def process_credit_card(user_token: str, amount: float):
    """Processes financial operations. Relies entirely on the auth vault function."""
    is_valid = validate_vault_token(user_token)
    if not is_valid:
        raise PermissionError("Security token invalid!")
    print(f"💳 [Gateway] Successfully transferred ${amount}")
