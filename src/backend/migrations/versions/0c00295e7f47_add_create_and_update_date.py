"""Add create and update date

Revision ID: 0c00295e7f47
Revises: dc99156466ae
Create Date: 2024-02-11 13:49:34.424456

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c00295e7f47'
down_revision: Union[str, None] = 'dc99156466ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("created_at", sa.DateTime))

def downgrade() -> None:
    op.drop_column("posts", "created_at")
