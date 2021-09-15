import { Component, OnInit, Input } from '@angular/core';
import { ProductoComponent } from '../producto/producto.component';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { ApiPagosServicio } from 'src/app/servicios/api/api-pagos.service';

@Component({
  selector: 'app-pago',
  templateUrl: './pago.component.html',
  styleUrls: ['./pago.component.css']
})
export class PagoComponent implements OnInit {

  
  precio:number= 0;
  nombrecli:string="";
  ced:string="";
  cuenta:string="";


  constructor(private router: Router,private http: HttpClient,private pagoservicio:ApiPagosServicio) {
    //this.getAllTasks
   }

  ngOnInit(
  ): void {

    this.precio = Math.round(Number( sessionStorage.getItem("tpvp")) * 100 )/ 100;
    console.log(`precio ${this.precio}`)

    this.nombrecli =  String(sessionStorage.getItem("nombre"));
    console.log(`nombrecliente ${this.nombrecli}`)

    this.ced =  String(sessionStorage.getItem("cedula"));
    console.log(`nombrecliente ${this.ced}`)

      }


    enviar(){

      //this.router.navigate(['login']);

      let idc: string = "" + this.ced;
      sessionStorage.setItem("cedula", idc);
      let cuenta: string = "" + this.cuenta;
      sessionStorage.setItem("cuenta", cuenta);
      

      
      this.pagoservicio.validarcuenta(idc,cuenta).subscribe(
        respuestaverificacion => {
          
          console.log(respuestaverificacion.token);
          let token=respuestaverificacion.token
          this.pagoservicio.pagarbanco(token,String(this.precio)).subscribe(
            repuestapago => {
              console.log("aquiiii",repuestapago);
              if (repuestapago.code==0) {
                
                  alert('pago realizado exitosamente');
                } else {
                  alert('error al realizar pago');
                }
              },
              errorpago=>{
                console.error(errorpago);
              }
              )
            },
        error=>{
          if(error.status == 404) {
           
            alert('error 404');
          } else {
            alert('error 404 negativo');
          
          }
        }

      )

      /*let idSupermercado = sessionStorage.getItem("id");
      console.log("cuenta",cuenta);
      console.log("idc",idc);*/


    }

  }
