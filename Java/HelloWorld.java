public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("=================================");
        System.out.println("  Bem-vindo ao meu repositório!  ");
        System.out.println("=================================");
        System.out.println();
        
        // Informações sobre o projeto
        String nome = "Meu Projeto Java";
        String versao = "1.0.0";
        String autor = "Seu Nome";
        
        System.out.println("Nome do Projeto: " + nome);
        System.out.println("Versão: " + versao);
        System.out.println("Autor: " + autor);
        System.out.println();
        
        // Uma calculadora simples
        System.out.println("--- Calculadora Simples ---");
        int a = 10;
        int b = 5;
        
        System.out.println("Soma: " + a + " + " + b + " = " + (a + b));
        System.out.println("Subtração: " + a + " - " + b + " = " + (a - b));
        System.out.println("Multiplicação: " + a + " * " + b + " = " + (a * b));
        System.out.println("Divisão: " + a + " / " + b + " = " + (a / b));
        System.out.println();
        
        // Array de exemplo
        System.out.println("--- Linguagens de Programação ---");
        String[] linguagens = {"Java", "Python", "JavaScript", "C++", "Go"};
        
        for (int i = 0; i < linguagens.length; i++) {
            System.out.println((i + 1) + ". " + linguagens[i]);
        }
        
        System.out.println();
        System.out.println("Obrigado por visitar meu repositório!");
    }
}