import os
from azure.cosmos import CosmosClient, ContainerProxy


def initialize_cosmos(cosmos_env_var : str, database_name : str, container_name : str) -> ContainerProxy:
    cosmos_endpoint = os.getenv(f"{cosmos_env_var}_COSMOS_URI")
    if cosmos_endpoint is None:
        raise Exception(f"Coudn't find Cosmos DB credentials in environment variable {cosmos_env_var}_COSMOS_URI")
    
    key = os.getenv(f"{cosmos_env_var}_COSMOS_KEY")
    client = CosmosClient(cosmos_endpoint, credential=key)
    # Connect to the Azure Cosmos DB container that has the questions
    database = client.get_database_client(database_name)
    container_client = database.get_container_client(container_name)

    return container_client