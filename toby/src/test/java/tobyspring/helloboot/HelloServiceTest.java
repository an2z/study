package tobyspring.helloboot;

import static org.assertj.core.api.Assertions.*;

import org.junit.jupiter.api.Test;

class HelloServiceTest {
	@Test
	void simpleHelloService() {
		SimpleHelloService helloService = new SimpleHelloService();
		String result = helloService.sayHello("Test");
		assertThat(result).isEqualTo("Hello Test");
	}
}