"""empty message

Revision ID: d37badff41ad
Revises: 926891cdc74a
Create Date: 2023-07-26 20:01:13.106636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd37badff41ad'
down_revision = '926891cdc74a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.alter_column('name_fantasy',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.drop_constraint('company_cnae_key', type_='unique')
        batch_op.create_unique_constraint(None, ['cnpj'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('company_cnae_key', ['cnae'])
        batch_op.alter_column('name_fantasy',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###
