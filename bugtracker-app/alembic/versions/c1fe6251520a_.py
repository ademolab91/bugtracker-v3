"""empty message

Revision ID: c1fe6251520a
Revises: 4018eaf87c09
Create Date: 2023-08-06 09:41:08.980304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'c1fe6251520a'
down_revision: Union[str, None] = '4018eaf87c09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    op.drop_table('ticket')
    op.drop_table('user')
    op.drop_table('comment')
    op.drop_table('tickethistory')
    op.drop_table('attachment')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attachment',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.Column('file_name', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.Column('file_path', sa.VARCHAR(), nullable=False),
    sa.Column('ticket_id', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tickethistory',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.Column('action', sa.VARCHAR(), nullable=False),
    sa.Column('previous_value', sa.VARCHAR(), nullable=False),
    sa.Column('present_value', sa.VARCHAR(), nullable=False),
    sa.Column('made_by', sa.VARCHAR(), nullable=True),
    sa.Column('ticket_id', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['made_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.Column('content', sa.VARCHAR(), nullable=False),
    sa.Column('ticket_id', sa.VARCHAR(), nullable=True),
    sa.Column('commenter_id', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['commenter_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('role', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('password', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.Column('submitter_id', sa.VARCHAR(), nullable=True),
    sa.Column('project_id', sa.VARCHAR(), nullable=True),
    sa.Column('assigned_developer_id', sa.VARCHAR(), nullable=True),
    sa.Column('ticket_type', sa.VARCHAR(), nullable=False),
    sa.Column('priority', sa.VARCHAR(), nullable=False),
    sa.Column('status', sa.VARCHAR(), nullable=False),
    sa.ForeignKeyConstraint(['assigned_developer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['submitter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.Column('creator_id', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###