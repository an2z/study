package src.fire.ch19;

/* 얕은 복사 (Shallow Copy)
 * 주소 값을 복사한다는 의미
 * 참조하고 있는 실제값이 같음
 */
class ShallowCopy {
    public static void main(String[] args) {
        Rectangle org = new Rectangle(1, 1, 9, 9);
        Rectangle cpy;

        try {
            cpy = (Rectangle) org.clone(); // 인스턴스 복사
            org.changePos(2, 2, 7, 7); // 인스턴스 좌표 정보 수정

            System.out.println("---- org 좌표 ----");
            org.showPosition();

            System.out.println("---- cpy 좌표 ----");
            cpy.showPosition();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
    }

    static class Point implements Cloneable {
        private int xPos;
        private int yPos;

        public Point(int x, int y) {
            xPos = x;
            yPos = y;
        }

        public void showPosition() {
            System.out.printf("[%d, %d]", xPos, yPos);
            System.out.println();
        }

        public void changePos(int x, int y) {
            xPos = x;
            yPos = y;
        }

        @Override
        public Object clone() throws CloneNotSupportedException {
            return super.clone();
        }
    }


    static class Rectangle implements Cloneable {
        private Point upperLeft; // 좌측 상단 좌표
        private Point lowerRight; // 우측 하단 좌표

        public Rectangle(int x1, int y1, int x2, int y2) {
            upperLeft = new Point(x1, y1);
            lowerRight = new Point(x2, y2);
        }

        public void changePos(int x1, int y1, int x2, int y2) { // 좌표 정보 수정
            upperLeft.changePos(x1, y1);
            lowerRight.changePos(x2, y2);
        }

        @Override
        public Object clone() throws CloneNotSupportedException {
            return super.clone();
        }

        public void showPosition() { // 직사각형 좌표 정보 출력
            System.out.print("좌측 상단 : ");
            upperLeft.showPosition();

            System.out.print("우측 하단 : ");
            lowerRight.showPosition();
        }
    }
}