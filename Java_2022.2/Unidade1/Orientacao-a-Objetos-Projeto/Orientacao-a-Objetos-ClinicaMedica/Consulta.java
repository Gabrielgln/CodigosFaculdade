class Consulta{
  public String data, hora;
  public Paciente paciente;
  public Medico medico;
  
  public Consulta(){};

  public Consulta(String data, String hora,Paciente paciente,Medico medico){
    this.data = data;
    this.hora = hora;
    this.paciente = paciente;
    this.medico = medico;
  }
  public String toString(){
    return "\nData: " + data +
      "\nHora:  " + hora +
      "\nPaciente: " + paciente +
      "\nMedico: " + medico;
  }
}



