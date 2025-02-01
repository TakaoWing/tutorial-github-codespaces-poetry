from azure.cosmos import CosmosClient, exceptions

# Initialize the Cosmos client
endpoint = "https://localhost:8081/"
key = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="
client = CosmosClient(endpoint, key)

# Create a database
database_name = "YourDatabaseName"
try:
    database = client.create_database_if_not_exists(id=database_name)
    print(f"Database '{database_name}' created successfully.")
except exceptions.CosmosResourceExistsError:
    print(f"Database '{database_name}' already exists.")
except exceptions.CosmosHttpResponseError as e:
    print(f"An error occurred: {e.message}")
