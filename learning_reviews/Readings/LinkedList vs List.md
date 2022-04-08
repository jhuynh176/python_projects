# Original answer...
I found interesting results:

```
// Temporary class to show the example
class Temp
{
    public decimal A, B, C, D;

    public Temp(decimal a, decimal b, decimal c, decimal d)
    {
        A = a;            B = b;            C = c;            D = d;
    }
}
```

## Linked list (3.9 seconds)
```
        LinkedList<Temp> list = new LinkedList<Temp>();

        for (var i = 0; i < 12345678; i++)
        {
            var a = new Temp(i, i, i, i);
            list.AddLast(a);
        }

        decimal sum = 0;
        foreach (var item in list)
            sum += item.A;
```

## List (2.4 seconds)
```
        List<Temp> list = new List<Temp>(); // 2.4 seconds

        for (var i = 0; i < 12345678; i++)
        {
            var a = new Temp(i, i, i, i);
            list.Add(a);
        }

        decimal sum = 0;
        foreach (var item in list)
            sum += item.A;
```

Even if you only access data essentially it is much slower!! I say never use a linkedList.

Here is another comparison performing a lot of inserts (we plan on inserting an item at the middle of the list)

## Linked List (51 seconds)
```
        LinkedList<Temp> list = new LinkedList<Temp>();

        for (var i = 0; i < 123456; i++)
        {
            var a = new Temp(i, i, i, i);

            list.AddLast(a);
            var curNode = list.First;

            for (var k = 0; k < i/2; k++) // In order to insert a node at the middle of the list we need to find it
                curNode = curNode.Next;

            list.AddAfter(curNode, a); // Insert it after
        }

        decimal sum = 0;
        foreach (var item in list)
            sum += item.A;
```

## List (7.26 seconds)
```
        List<Temp> list = new List<Temp>();

        for (var i = 0; i < 123456; i++)
        {
            var a = new Temp(i, i, i, i);

            list.Insert(i / 2, a);
        }

        decimal sum = 0;
        foreach (var item in list)
            sum += item.A;
```

## Linked List having reference of location where to insert (.04 seconds)
```
        list.AddLast(new Temp(1,1,1,1));
        var referenceNode = list.First;

        for (var i = 0; i < 123456; i++)
        {
            var a = new Temp(i, i, i, i);

            list.AddLast(a);
            list.AddBefore(referenceNode, a);
        }

        decimal sum = 0;
        foreach (var item in list)
            sum += item.A;
```

So only if you plan on inserting several items and you also somewhere have the reference of where you plan to insert the item then use a linked list. Just because you have to insert a lot of items it does not make it faster because searching the location where you will like to insert it takes time.