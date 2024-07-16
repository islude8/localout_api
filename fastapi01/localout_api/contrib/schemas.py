from pydantic import BaseModel


class BaseSchema[BaseModel]:
    class Config:
        extra = 'forbid' #Proibir valores diferentes nas lacunas
        from_atributes = True #Converter models para schemes