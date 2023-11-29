"""add customers date_of_birth

Revision ID: f0c0d3260756
Revises: fcecd47ce3fe
Create Date: 2023-11-23 14:36:48.754301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f0c0d3260756"
down_revision = "fcecd47ce3fe"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
