import inspect
from findex.stats import iter_documents
from findex.tokenize import tokenize

print("Is iter_documents a generator?", inspect.isgeneratorfunction(iter_documents))
print("Is tokenize a generator?", inspect.isgeneratorfunction(tokenize))
