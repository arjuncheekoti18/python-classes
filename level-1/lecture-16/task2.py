def register_player(player_name, game="minecraft", *accessories):
    final_amount = 0
    game_price=0
    match game:
        case "mincraft":
            game_price = 200
        case "fifa":
            game_price = 300
        case "valorant":
            game_price = 400
    number_of_accessories = len(accessories)
    accessories_price = number_of_accessories * 50
    final_amount = accessories_price + game_price
    discount=0
    if game == "valorant" and number_of_accessories > 3:
        discount = (15/100) * final_amount
        final_amount = final_amount - discount
    bill = f"""
    player name: {player_name}
    game: {game}
    accessories: {accessories}
    game price: ₹{game_price}
    cost of accessories: ₹{accessories_price}
    discount: ₹{discount}
    final bill: ₹{final_amount}
    """
    print(bill)
register_player("Ryan", "valorant", "gaming headset", "gaming mouse", "mechanical keybord", "rgb lights")