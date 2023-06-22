from azure.cosmos import CosmosClient, PartitionKey, exceptions

class CosmosDbService:
    def __init__(self, endpoint, key, database_name, container_name):
        self.client = CosmosClient(endpoint, key)
        self.database_client = self.client.get_database_client(database_name)
        try:
            self.container = self.database_client.get_container_client(container_name)
            # Try to read the container to see if it exists
            self.container.read()
        except exceptions.CosmosResourceNotFoundError:
            # If the container does not exist, create it
            self.container = self.database_client.create_container_if_not_exists(
                id=container_name,
                partition_key=PartitionKey(path="/partition_key")
            )
