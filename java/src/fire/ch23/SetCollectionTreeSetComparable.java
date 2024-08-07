package src.fire.ch23;

import java.util.TreeSet;

/* TreeSet의 정렬 기준 마련 (Comparable 인터페이스 구현) */
class SetCollectionTreeSetComparable {
    public static void main(String[] args) {
        TreeSet<Person> tree = new TreeSet<>();

        tree.add(new Person("anne", 26));
        tree.add(new Person("wuga", 26));
        tree.add(new Person("jeong", 25));
        tree.add(new Person("jun", 27));

        for (Person p : tree) {
            System.out.println(p + " ");
        }

        System.out.println(new Person("anne", 26).equals(new Person("wuga", 26)));
    }

    static class Person implements Comparable<Person> {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        @Override
        public String toString() {
            return name + " : " + age;
        }

        @Override
        public int compareTo(Person p) {
            return this.age - p.age;
        }
    }
}
