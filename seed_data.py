# seed_data.py
from app import create_app
from extensions import db
from models.product import Product

app = create_app()

def seed_database():
    """
    Automated Seeding System: Injects certified mock products into the SQL database file.
    """
    print("Initiating Khatri AgroVet database inventory injection procedure...")
    
    with app.app_context():
        # Safeguard: Check if records are already present to avoid duplication
        if Product.query.count() > 0:
            print("Database already contains product entries. Seeding operation aborted.")
            return

        mock_products = [
            # Agricultural Segment Inputs
            Product(
                name="Premium Urea Fertilizer (50KG)",
                category="Agro",
                price=299.50,
                stock=140,
                description="High-nitrogen structural field fertilizer designed to accelerate vegetative canopy scaling and leaf chlorophyll development."
            ),
            Product(
                name="Hybrid Non-GMO Maize Seeds (10KG)",
                category="Agro",
                price=850.00,
                stock=45,
                description="Certified weather-resilient maize kernels featuring enhanced early root structure development for optimal seasonal crop yields."
            ),
            Product(
                name="Broad-Spectrum Organic Pesticide (1L)",
                category="Agro",
                price=450.00,
                stock=60,
                description="Eco-friendly targeted protection compound. Suppresses aphid and caterpillar outbreaks without degrading local soil microbiomes."
            ),
            
            # Veterinary Segment Inputs
            Product(
                name="High-Protein Cattle Feed Booster",
                category="Vet",
                price=1200.00,
                stock=35,
                description="Premium nutrient feed block loaded with essential amino acids, calcium, and trace minerals to maximize daily livestock milk yield."
            ),
            Product(
                name="Avian Multivitamin Feed Supplement",
                category="Vet",
                price=320.00,
                stock=110,
                description="Water-soluble immune system formula optimized for poultry layers to reinforce eggshell thickness and metabolic efficiency."
            ),
            Product(
                name="Antiseptic Veterinary Wound Spray",
                category="Vet",
                price=180.00,
                stock=0,  # Intentional out-of-stock item to verify UI display
                description="Rapid-action topical disinfectant spray intended for livestock abrasions, cuts, and minor surgical patch processing operations."
            )
        ]

        # Stage and commit data entries
        db.session.add_all(mock_products)
        db.session.commit()
        print("Success! 6 Premium products successfully committed to khatri_agrovet.db.")

if __name__ == '__main__':
    seed_database()