/*
 * @Author       : Yida
 * @Date         : 2020-03-01 20:28:21
 * @Description  : Test the data structure.
 */


class Test {

    public static void main(final String[] args) {
        final Queue myQueue = new Queue();
        myQueue.add(1);
        myQueue.add(2);
        myQueue.add(3);
        myQueue.add(4);
        myQueue.add(5);
        System.out.println(myQueue.size());
        System.out.println(myQueue.getPointer());
        myQueue.poll();
        myQueue.poll();
        myQueue.poll();
        System.out.println(myQueue.getPointer());
        myQueue.poll();
        myQueue.poll();
        System.out.println(myQueue.poll());
        System.out.println(myQueue.getPointer());
    }
}