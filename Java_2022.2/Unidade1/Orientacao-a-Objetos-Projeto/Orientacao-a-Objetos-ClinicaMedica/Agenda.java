import java.util.List;
import java.util.ArrayList;

public class Agenda{
  private ArrayList<Consulta> consultas = new ArrayList<Consulta>();

  public Agenda(){}

  public Agenda(ArrayList<Consulta> consultas){
    this.consultas = consultas;
  }

  public int verificarConsulta(Consulta c_cliente){
    for(Consulta c: consultas){
      if (c_cliente.data == c.data && c_cliente.hora == c.hora && c_cliente.medico == c.medico){
        return 1;
      }   
    }
    return 2;
  }

  public void cadastrarConsulta(Consulta c_cliente){
    if(this.verificarConsulta(c_cliente) == 2){
      this.consultas.add(c_cliente);
    }
    else{
      System.out.println("Já existe consulta nesta data e horario!");
    }   
  }

  public void imprime(){
    for(Consulta c : consultas){
      System.out.println(c);
    }
  }

}
  