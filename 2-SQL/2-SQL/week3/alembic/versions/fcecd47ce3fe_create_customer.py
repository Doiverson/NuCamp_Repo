"""create customer

Revision ID: fcecd47ce3fe
Revises: 
Create Date: 2023-11-23 14:20:43.591428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fcecd47ce3fe"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
