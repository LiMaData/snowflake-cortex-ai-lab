
import os
import sys
from dotenv import load_dotenv
from snowflake.snowpark import Session

# Load environment variables
load_dotenv()

def get_session():
    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": os.getenv("SNOWFLAKE_ROLE"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA")
    }
    return Session.builder.configs(connection_parameters).create()

def deploy():
    print("Starting Semantic Model Deployment...")
    session = get_session()
    
    try:
        # 1. Ensure Stage Exists
        stage_name = "semantic_models" # Or get from env: os.getenv("SEMANTIC_MODEL_STAGE_NAME", "semantic_models")
        
        # Note: If user provided a path like @folder/file.yaml in .env, we extract the stage name
        # But simpler to just ensure the stage 'semantic_models' exists for now.
        print(f"Ensuring stage '{stage_name}' exists...")
        session.sql(f"CREATE STAGE IF NOT EXISTS {stage_name}").collect()
        
        # 2. Upload File
        local_file = "config/semantic.yaml"
        # We upload to the stage. PUT command returns a list of upload results.
        print(f"Uploading '{local_file}' to @{stage_name}...")
        put_result = session.file.put(local_file, f"@{stage_name}", auto_compress=False, overwrite=True)
        print(f"   Upload status: {put_result[0].status}")

        # 3. Create/Update Semantic Model Object
        # We need the relative path of the file in the stage. 
        # file.put uploads 'semantic.yaml' -> @semantic_models/semantic.yaml
        object_name = "SFMC_EMAIL_PERFORMANCE"
        stage_path = f"@{stage_name}"
        main_file = "semantic.yaml"
        
        print(f"Updating Semantic Model Object '{object_name}'...")
        
        create_sql = f"""
        CREATE OR REPLACE SEMANTIC MODEL {object_name}
        FROM '{stage_path}'
        MAIN_FILE = '{main_file}'
        """
        session.sql(create_sql).collect()
        
        print("Deployment Complete!")
        
        # Optional: Describe to verify
        # session.sql(f"DESCRIBE SEMANTIC MODEL {object_name}").show()

    except Exception as e:
        print(f"Error during deployment: {e}")
        sys.exit(1)
    finally:
        session.close()

if __name__ == "__main__":
    deploy()
