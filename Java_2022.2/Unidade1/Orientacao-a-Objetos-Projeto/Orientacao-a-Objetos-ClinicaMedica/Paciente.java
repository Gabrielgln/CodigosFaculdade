public class Paciente{
  public String nome, idade;

  public Paciente(){  
  }

  public Paciente(String nome, String idade){
    this.nome = nome;
    this.idade = idade;
  }

  public String toString(){
    return "\nNome: " + nome + "\nIdade: " + this.idade;
  }
}