class Medico{
  private String nome;
  private String crm;
  private Agenda agenda;
   
  public Medico() {}
  
  public Medico(String nome, String crm) {
    this.nome = nome;
    this.crm = crm;
    this.agenda = new Agenda();
  }

  public void imprime(){
    agenda.imprime();
  }

  public void cadastrarConsulta(Consulta c_cliente){
    agenda.cadastrarConsulta(c_cliente);
  }

public String toString(){
  return "\nNome: " +nome+ "\nCRM: " +crm;
  }
}
