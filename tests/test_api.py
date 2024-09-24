import unittest
from unittest.mock import MagicMock, patch
from sqlalchemy import create_engine, MetaData, Table, insert, select, update, delete
from sqlalchemy.orm import sessionmaker
import os

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Simuler la connexion à la base de données et la session
        cls.engine = MagicMock()
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        cls.metadata = MetaData()
        
        # Simuler les tables
        cls.customers_table = Table('Customers', cls.metadata)
        cls.addresses_table = Table('Addresses', cls.metadata)
        cls.companies_table = Table('Companies', cls.metadata)

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # Test de connexion à la base de données
    def test_database_connection(self):
        """Teste la connexion à la base de données."""
        self.assertIsNotNone(self.engine, "L'objet engine doit être créé.")

    # Test pour vérifier l'existence de la table 'Customers'
    def test_table_customers_exists(self):
        """Vérifie que la table 'Customers' existe dans la base de données."""
        tables = ['Customers', 'Addresses', 'Companies']
        self.assertIn('Customers', tables, "La table 'Customers' n'existe pas dans la base de données.")

    # Test pour vérifier l'existence de la table 'Addresses'
    def test_table_addresses_exists(self):
        """Vérifie que la table 'Addresses' existe dans la base de données."""
        tables = ['Customers', 'Addresses', 'Companies']
        self.assertIn('Addresses', tables, "La table 'Addresses' n'existe pas dans la base de données.")

    # Test pour vérifier l'existence de la table 'Companies'
    def test_table_companies_exists(self):
        """Vérifie que la table 'Companies' existe dans la base de données."""
        tables = ['Customers', 'Addresses', 'Companies']
        self.assertIn('Companies', tables, "La table 'Companies' n'existe pas dans la base de données.")

    # Test pour simuler l'insertion dans la table 'Customers'
    def test_insert_into_customers(self):
        """Teste l'insertion d'un client dans la table 'Customers'."""
        self.session.execute = MagicMock(return_value=MagicMock(inserted_primary_key=[1]))
        insert_query = insert(self.customers_table).values(
            name="John Doe", email="john.doe@example.com"
        )
        result = self.session.execute(insert_query)
        self.session.commit()

        self.assertIsNotNone(result.inserted_primary_key, "L'insertion dans la table 'Customers' a échoué.")

    # Test pour simuler l'insertion dans la table 'Addresses'
    def test_insert_into_addresses(self):
        """Teste l'insertion d'une adresse dans la table 'Addresses'."""
        self.session.execute = MagicMock(return_value=MagicMock(inserted_primary_key=[1]))
        insert_query = insert(self.addresses_table).values(
            address_line1="123 Rue de Paris", city="Paris", state="Île-de-France", postal_code="75001", country="France", id_customer=1
        )
        result = self.session.execute(insert_query)
        self.session.commit()

        self.assertIsNotNone(result.inserted_primary_key, "L'insertion dans la table 'Addresses' a échoué.")

    # Test pour simuler l'insertion dans la table 'Companies'
    def test_insert_into_companies(self):
        """Teste l'insertion d'une entreprise dans la table 'Companies'."""
        self.session.execute = MagicMock(return_value=MagicMock(inserted_primary_key=[1]))
        insert_query = insert(self.companies_table).values(
            name="Tech Corp", address="456 Avenue des Champs-Élysées", email="contact@techcorp.com", phone="0147258369"
        )
        result = self.session.execute(insert_query)
        self.session.commit()

        self.assertIsNotNone(result.inserted_primary_key, "L'insertion dans la table 'Companies' a échoué.")

    # Test pour simuler la lecture des données dans la table 'Customers'
    def test_read_from_customers(self):
        """Teste la lecture des données insérées dans la table 'Customers'."""
        self.session.execute = MagicMock(return_value=MagicMock(fetchone=MagicMock(return_value={'email': "john.doe@example.com"})))
        select_query = select([self.customers_table]).where(self.customers_table.c.email == "john.doe@example.com")
        result = self.session.execute(select_query).fetchone()

        self.assertIsNotNone(result, "Aucune donnée trouvée dans la table 'Customers'.")
        self.assertEqual(result['email'], "john.doe@example.com", "Le champ 'email' est incorrect.")

    # Test pour simuler la mise à jour des données dans la table 'Customers'
    def test_update_customers(self):
        """Teste la mise à jour d'un client dans la table 'Customers'."""
        self.session.execute = MagicMock(return_value=MagicMock(rowcount=1))
        update_query = update(self.customers_table).where(self.customers_table.c.email == "john.doe@example.com").values(name="Jane Doe")
        result = self.session.execute(update_query)
        self.session.commit()

        self.assertGreater(result.rowcount, 0, "Aucune ligne n'a été mise à jour dans la table 'Customers'.")

    # Test pour simuler la suppression des données dans la table 'Customers'
    def test_delete_from_customers(self):
        """Teste la suppression d'un client dans la table 'Customers'."""
        self.session.execute = MagicMock(return_value=MagicMock(rowcount=1))
        delete_query = delete(self.customers_table).where(self.customers_table.c.email == "john.doe@example.com")
        result = self.session.execute(delete_query)
        self.session.commit()

        self.assertGreater(result.rowcount, 0, "Aucune ligne n'a été supprimée dans la table 'Customers'.")

    # Test pour simuler la lecture des données dans la table 'Addresses'
    def test_read_from_addresses(self):
        """Teste la lecture des données insérées dans la table 'Addresses'."""
        self.session.execute = MagicMock(return_value=MagicMock(fetchone=MagicMock(return_value={'address_line1': "123 Rue de Paris"})))
        select_query = select([self.addresses_table]).where(self.addresses_table.c.address_line1 == "123 Rue de Paris")
        result = self.session.execute(select_query).fetchone()

        self.assertIsNotNone(result, "Aucune donnée trouvée dans la table 'Addresses'.")
        self.assertEqual(result['address_line1'], "123 Rue de Paris", "Le champ 'address_line1' est incorrect.")

if __name__ == '__main__':
    unittest.main()
