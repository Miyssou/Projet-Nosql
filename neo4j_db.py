from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD


class Neo4jDB:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def create_person(self, name):

        query = """
        CREATE (p:Person {name:$name})
        """

        with self.driver.session() as session:
            session.run(query, name=name)

    def create_relation(self, name1, name2):

        query = """
        MATCH (a:Person {name:$name1}),
              (b:Person {name:$name2})
        CREATE (a)-[:KNOWS]->(b)
        """

        with self.driver.session() as session:
            session.run(query, name1=name1, name2=name2)

    def get_relations(self):

        query = """
        MATCH (a)-[r]->(b)
        RETURN a.name, type(r), b.name
        """

        with self.driver.session() as session:
            return session.run(query)