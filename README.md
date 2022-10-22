# Async Views

When using Django 4.1 and above, REST framework allows you to work with async class and function based views.

For class based views, all handler methods must be async, otherwise Django will raise an exception. For function based views, the function itself must be async.

For example:

    from 

    class AsyncView(APIView):
        async def get(self, request):
            return Response({"message": "This is an async class based view."})


    @api_view(['GET'])
    async def async_view(request):
        return Response({"message": "This is an async function based view."})