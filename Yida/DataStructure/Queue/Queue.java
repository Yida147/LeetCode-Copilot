import java.util.ArrayList;

/*
 * @Author       : Yida
 * @Date         : 2020-03-01 20:15:38
 * @Description  : My queue
 */
class Queue {
    private final ArrayList<Integer> elements;
    private int pointer;

    public Queue() {
        this.elements = new ArrayList<>();
    }

    public int getPointer() {
        return pointer;
    }

    public int size() {
        return this.elements.size() - pointer;
    }

    public boolean empty() {
        return this.size() == 0;
    }

    public void add(final Integer e) {
        this.elements.add(e);
    }

    public Integer poll() {
        if (this.empty()) {
            return null;
        }
        return this.elements.get(pointer++);
    }
}