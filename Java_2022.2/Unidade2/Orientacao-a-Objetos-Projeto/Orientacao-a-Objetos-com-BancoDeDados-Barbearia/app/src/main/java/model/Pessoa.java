/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author gabri
 */
public class Pessoa {
    
  private String nome;
  private String email;
  private String telefone;

  //Construto vazio:
  public Pessoa(){}

  //Construtor:
  public Pessoa(String nome,String email,String telefone){
    this.nome = nome;
    this.email = email;
    this.telefone = telefone;
  }

  //Acessores:
  public void setNome(String nome){
    this.nome = nome;
  }
  public String getNome(){
    return nome;
  }

  public void setEmail(String email){
    this.email = email;
  }
  public String getEmail(){
    return email;
  }

  public void setTelefone(String telefone){
    this.telefone = telefone;
  }
  public String getTelefone(){
    return telefone;
  }

  //toString:
  public String toString(){
    return "\nNome: "+nome+
      "\nEmail: "+email+
      "\nTelefone: "+telefone;
  }
}
