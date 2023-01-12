class Main {
  public static void main(String[] args) {
    Paciente p1 = new Paciente("Adrier","20");
    Medico m1 = new Medico("Joao", "202020PB");
    Medico m2 = new Medico("gabriel", "202020PB");
    
    Consulta c1 = new Consulta("22.10.2022", "16:00", p1, m1);
    Consulta c2 = new Consulta("22.10.2022", "16:00", p1, m2);
    
    m1.cadastrarConsulta(c1);
    m1.cadastrarConsulta(c2);
    m1.imprime();
  
  }
}  