/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author gabri
 */
public class DataHora {
    
  private String registro;

  //Construtor vazio:
  public DataHora(){}
  
  //Construto:
  public DataHora(String registro){
    this.registro = registro;
  }

  //Acessores:
  public void setRegistro(String registro){
    this.registro = registro;
  }

  public String getRegistro(){
    return registro;
  }

  //toString:
  public String toString(){
    return "\nData Hora: "+registro;
  }
}
