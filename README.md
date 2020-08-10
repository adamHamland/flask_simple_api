# Employee Registry service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all employees

**Definitions**

`GET /employees`

**Responce**

- `200 OK` on success

```json
[
    {
        "ssid": "111111111",
        "name": "John Smith",
        "role": "CEO"
    },
    {
        "ssid": "222222222",
        "name": "Jane Smith",
        "role": "CFO"
    }
]
```

### Registering a new device

**Definition**

`POST /employees`

**Arguments**

- `"ssid":string` a 9 digit social security nuber
- `"name":string` the full name of the employee
- `"role":string` the name of the job they currently hold

If a employee with the given ssid already exists, it will be overwritten with the new data.

**Response**

- `201 Created` on success

```json
{
    "ssid": "111111111",
    "name": "John Smith",
    "role": "CEO"
}
```

## Lookup employee details

`GET /employee/<ssid>`

**Responce**
- `404 Not Found` if the employee with the given ssid does not exist in the database
- `200 OK` on success

```json
{
    "ssid": "111111111",
    "name": "John Smith",
    "role": "CEO"
}
```

## Delete an employee

**Definition**

`DELETE /employee/<ssid>`
- `404 Not Found` if the employee with the given ssid does not exist in the database
- `204 No Content` if the employee was deleted succsessfully