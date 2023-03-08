
import os
from github import Github

 
async def add_github_permission(user_email: str, product_id: str):
    product_id_env = os.environ["PRODUCT_ID"]
    
    if product_id != product_id_env:
        g = Github(os.environ["GITHUB_TOKEN"])

        result = []
        organization = g.get_organization("do-zero-ao-mvp")
        team_name = 'zeros'
        # TYPES OF ROLES= ["admin", "direct_member", "billing_manager"], TEAMS is ARRAY
        try:
            teams = organization.get_teams()
            for t in teams:
                if t.name == team_name:
                    team = t
            result = organization.invite_user(email=user_email,
                    role="direct_member",
                    teams=[team])
        except Exception as error:
            raise error
        if result is None:
            print(f"Successfully sent invite")
