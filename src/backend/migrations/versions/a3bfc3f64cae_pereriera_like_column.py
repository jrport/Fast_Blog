"""pereriera_Like_column

Revision ID: a3bfc3f64cae
Revises: 0c00295e7f47
Create Date: 2024-02-14 18:42:10.681939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3bfc3f64cae'
down_revision: Union[str, None] = '0c00295e7f47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("perararea_liker", sa.String(50)))


def downgrade() -> None:
    op.drop_column("posts", "perararea_liker")
