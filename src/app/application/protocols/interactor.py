####################################################
# PEP695... доступно с 12 версии python            #
# По другому это выглядело бы так:                 #
# from typing import TypeVar, Generic              #
#                                                  #
# InputDTO = TypeVar('InputDTO')                   #
# OutputDTO = TypeVar('OutputDTO')                 #
#                                                  #
#                                                  #
# class Interactor(Generic[InputDTO, OutputDTO]):  #
#   ...                                            #
####################################################


class Interactor[InputDTO, OutputDTO]:
    """ Интерактор для разделения домена от уровня представления. """

    async def __call__(self, data: InputDTO) -> OutputDTO:
        raise NotImplementedError(
            'The child class does\'t not math the signature!'
        )
