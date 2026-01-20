
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
        # 1. Ensure Stages Exist
        # We ensure both 'SEMANTIC_MODELS' and 'SEMANTIC_FILES' exist to be safe
        for stage_name in ["SEMANTIC_MODELS", "SEMANTIC_FILES"]:
            print(f"Ensuring stage '{stage_name}' exists and has directory enabled...")
            session.sql(f"CREATE STAGE IF NOT EXISTS {stage_name}").collect()
            session.sql(f"ALTER STAGE {stage_name} SET DIRECTORY = (ENABLE = TRUE)").collect()
            session.sql(f"ALTER STAGE {stage_name} REFRESH").collect()
            
            # 2. Upload File
            local_file = "config/semantic.yaml"
            print(f"Uploading '{local_file}' to @{stage_name}...")
            put_result = session.file.put(local_file, f"@{stage_name}", auto_compress=False, overwrite=True)
            print(f"   Upload status to @{stage_name}: {put_result[0].status}")

        main_file = "semantic.yaml"
        print("\nDeployment Complete!")
        print(f"Your semantic model has been uploaded to both @SEMANTIC_MODELS and @SEMANTIC_FILES.")
        print(f"\nNext Steps in Snowsight:")
        print(f"1. Go to AI & ML -> Agents")
        print(f"2. Edit your Agent's 'Sales_Data' tool (Cortex Analyst)")
        print(f"3. Verify it points to: Snowcamp_DB -> [Your Schema] -> SEMANTIC_FILES -> {main_file}")

    except Exception as e:
        print(f"Error during deployment: {e}")
        sys.exit(1)
    finally:
        session.close()

if __name__ == "__main__":
    deploy()
