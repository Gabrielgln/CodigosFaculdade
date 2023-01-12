import java.util.ArrayList;
import java.util.Scanner;

public class Agenda{

  //atributos
  private static ArrayList<Agendamento> agendas = new ArrayList<Agendamento>();

  //Construtor vazio:
  public Agenda(){}

  //Construtor:
  public Agenda(ArrayList<Agendamento> agendas){
    this.agendas = agendas;  
  }

  Scanner leitor = new Scanner(System.in);

  //Função para inserir o agendamento na lista de agendamentos
  public void agendarHorario(Agendamento agendarCliente){
    this.agendas.add(agendarCliente);
  }

  //Função para imprimir relatorio de agendamentos:
  public void imprimirRelatorio(){
    for(Agendamento agendamento : agendas){
      System.out.println(agendamento);
    }
  }

  public void imprimirAgendamentoCliente(){
    
    for(Agendamento agendamentos : agendas){
      String verificacao_email;
      System.out.println("\nDigite o email para confirmação: ");
      verificacao_email = leitor.nextLine();
      if(agendamentos.getCliente().getEmail().equals(verificacao_email)){
        System.out.println(agendamentos);
        break;
      }
    }
  }

  //Acessores:
  public void setAgendas(ArrayList<Agendamento> agendas){
    this.agendas = agendas;
  }
  public ArrayList<Agendamento> getAgendas(){
    return this.agendas;
  }
  
}