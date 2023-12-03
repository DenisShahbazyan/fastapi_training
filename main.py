from fastapi import FastAPI, Body

from schemas import Person


app = FastAPI()


@app.post('/hello')
def greetings(
        person: Person = Body(
            ..., examples=Person.Config.schema_extra['examples']
        )
) -> dict[str, str]:
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}
