hired_employees_schema = {
    "doc": "Hired Employees",
    "name": "Hired Employees",
    "namespace": "Employees",
    "type": "record",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "name", "type": "string"},
        {
            "name": "datetime",
            "type": {"type": "string", "logicalType": "timestamp-micros"},
        },
        {"name": "department_id", "type": "int"},
        {"name": "job_id", "type": "long"},
    ],
}


hired_employees_columns = ["id", "name", "datetime", "department_id", "job_id"]


departments_schema = {
    "doc": "department",
    "name": "department",
    "namespace": "department",
    "type": "record",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "department", "type": "string"},
    ],
}


departments_columns = ["id", "department"]


jobs_schema = {
    "doc": "jobs",
    "name": "jobs",
    "namespace": "jobs",
    "type": "record",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "job", "type": "string"},
    ],
}


jobs_columns = ["id", "job"]