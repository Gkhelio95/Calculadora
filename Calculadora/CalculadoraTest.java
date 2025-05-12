:\Users\Adrian\Desktop\TareaEvaluable\CalculadoraTest.java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class CalculadoraTest {
    private Calculadora calculadora;
    private static final double DELTA = 0.001;

    @BeforeEach
    void setUp() {
        calculadora = new Calculadora();
    }

    @Test
    void testSumar() {
        assertEquals(5.0, calculadora.sumar(2.0, 3.0), DELTA);
    }

    @Test
    void testRestar() {
        assertEquals(6.0, calculadora.restar(10.0, 4.0), DELTA);
    }

    @Test
    void testMultiplicar() {
        assertEquals(21.0, calculadora.multiplicar(3.0, 7.0), DELTA);
    }

    @Test
    void testDividir() {
        assertEquals(5.0, calculadora.dividir(10.0, 2.0), DELTA);
    }

    @Test
    void testDividirPorCero() {
        assertThrows(ArithmeticException.class, () -> calculadora.dividir(5.0, 0.0));
    }

    @Test
    void testSumarNegativos() {
        assertEquals(-5.0, calculadora.sumar(-2.0, -3.0), DELTA);
    }

    @Test
    void testMultiplicarDecimales() {
        assertEquals(10.5, calculadora.multiplicar(2.5, 4.2), DELTA);
    }

    @Test
    void testDividirDecimales() {
        assertEquals(2.5, calculadora.dividir(5.5, 2.2), DELTA);
    }
}