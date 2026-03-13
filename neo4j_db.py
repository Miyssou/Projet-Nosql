from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD


class Neo4jDB:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    # créer un film
    def create_movie(self, title, year):

        query = """
        CREATE (m:Movie {title:$title, year:$year})
        """

        with self.driver.session() as session:
            session.run(query, title=title, year=year)


    # créer un acteur
    def create_actor(self, name):

        query = """
        CREATE (a:Actor {name:$name})
        """

        with self.driver.session() as session:
            session.run(query, name=name)


    # créer relation acteur -> film
    def create_acted_in(self, actor, movie):

        query = """
        MATCH (a:Actor {name:$actor}),
              (m:Movie {title:$movie})
        CREATE (a)-[:ACTED_IN]->(m)
        """

        with self.driver.session() as session:
            session.run(query, actor=actor, movie=movie)


    # récupérer les relations acteur-film
    def get_actor_movie_relations(self):

        query = """
        MATCH (a:Actor)-[r:ACTED_IN]->(m:Movie)
        RETURN a.name, m.title
        """

        with self.driver.session() as session:
            return session.run(query)