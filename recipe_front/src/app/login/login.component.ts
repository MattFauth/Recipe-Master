import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { UserService } from '../user.service';
import { Router } from '@angular/router';
import { concatMap, delay } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user: any;
  error: any;
  username = null;
  password = null;

  constructor(public auth$: AuthService, private user$: UserService, private router: Router) { }

  ngOnInit() {
    this.user = this.auth$.user();
    if (this.user){
      this.router.navigate(['/perfil']);
    }
  }

  login(){
    this.auth$.login(this.username, this.password)
      .pipe(
        delay(200),
        concatMap(() => this.auth$.getDetalhesDoUsuarioLogado())
      ).subscribe(
        () => this.router.navigate(['/perfil']),
        err => this.error = err.error
      );
  }

  refreshToken(){
    this.auth$.refreshToken().subscribe(
      user => {
        this.user = user;
        this.error = null;
      },
      error => {
        this.error = error.error;
        this.user = null;
      }
    );
  }

}
