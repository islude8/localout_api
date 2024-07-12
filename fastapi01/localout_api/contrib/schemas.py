from pydantic import BaseModel


class BaseSchema[BaseModel]:
    extra = 'forbid' #Proibir valores diferentes nas lacunas
    from_atributes = True #Converter models para schemes