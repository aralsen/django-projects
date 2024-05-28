# Adding Coins to the Database

To add some coins to the database using the Django ORM, follow these steps:

1. Open your Django shell via the terminal:

    ```bash
    python manage.py shell
    ```

2. Assuming this is done in a Django shell or in a data migration script, execute the following commands:

    ```python
    # Import the Coin model
    from coins.models import Coin

    # Create coin objects using the Coin model's create method
    Coin.objects.create(name='Bitcoin', photo_url='https://cryptologos.cc/logos/bitcoin-btc-logo.png?v=032')
    Coin.objects.create(name='Ethereum', photo_url='https://cryptologos.cc/logos/ethereum-eth-logo.png?v=032')
    Coin.objects.create(name='Solana', photo_url='https://cryptologos.cc/logos/solana-sol-logo.png?v=032')
    Coin.objects.create(name='Dogecoin', photo_url='https://cryptologos.cc/logos/dogecoin-doge-logo.png?v=032')
    ```

These commands will add four coins (Bitcoin, Ethereum, Solana, and Dogecoin) to the database. Replace the `photo_url` values with the appropriate URLs for the coin logos.
