from datetime import datetime, timedelta, timezone
import random
from dag_cost_tracker.db import init_db, get_session, get_db_url
from dag_cost_tracker.models import Base, DagRun, TaskCost
from sqlalchemy import create_engine

def seed():
    # Reset DB
    engine = create_engine(get_db_url())
    Base.metadata.drop_all(engine)
    init_db()
    
    session = get_session()
    
    dags = ["etl_daily", "ml_training", "report_generation"]
    warehouses = ["SMALL", "LARGE", "XL"]
    
    # Generate last 10 days of runs
    for i in range(10):
        # Use timezone-aware UTC
        date = datetime.now(timezone.utc) - timedelta(days=i)
        for dag in dags:
            run_id = f"run_{date.strftime('%Y%m%d')}_{dag}"
            
            dag_run = DagRun(
                dag_id=dag,
                run_id=run_id,
                execution_date=date,
                total_cost=0,
                duration_seconds=0,
                task_count=0
            )
            session.add(dag_run)
            session.flush()
            
            total_cost = 0
            count = 0
            total_duration = 0
            
            # 5 tasks per dag
            for t in range(5):
                duration = random.randint(60, 3600)
                wh = random.choice(warehouses)
                # Mock cost: assume 1 credit/hr, $3/credit approx (simplified)
                cost = (duration/3600) * 1 * 3
                if wh == "LARGE": cost *= 2
                if wh == "XL": cost *= 4
                
                task_cost = TaskCost(
                    dag_run_id=dag_run.id,
                    task_id=f"task_{t}",
                    warehouse_name=wh,
                    duration_seconds=duration,
                    cost=cost,
                    start_time=date,
                    end_time=date + timedelta(seconds=duration)
                )
                session.add(task_cost)
                
                total_cost += cost
                total_duration += duration
                count += 1
            
            dag_run.total_cost = total_cost
            dag_run.duration_seconds = total_duration
            dag_run.task_count = count
            
    session.commit()
    print("Seeded database with sample data.")

if __name__ == "__main__":
    seed()
