from pydantic import BaseModel


class User(BaseModel):
    id: int
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return '{id},{f_name},{l_name}'\
            .format(
                id=self.id,
                f_name=self.first_name,
                l_name=self.last_name
            )


