# Overview

Adds async support to Django REST Framework.

Currently not production ready. Use at your own risk :)

# Requirements

- Python 3.10+
- Django 4.1+

# Installation

```
pip install django-rest-framework-async
```

# Example

```python
from drfa.decorators import api_view
from drfa.views import APIView

class AsyncView(APIView):
    async def get(self, request):
        return Response({"message": "This is an async class based view."})


@api_view(['GET'])
async def async_view(request):
    return Response({"message": "This is an async function based view."})
```