import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { TopGeneralFeedComponent } from './top-general-feed/top-general-feed.component';
import { TopTargetedFeedComponent } from './top-targeted-feed/top-targeted-feed.component';

import { MatButtonModule, MatToolbarModule, MatIconModule, MatMenuModule } from '@angular/material';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';

library.add(faCoffee);

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    TopGeneralFeedComponent,
    TopTargetedFeedComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MatButtonModule,
    MatToolbarModule,
    MatIconModule,
    FontAwesomeModule,
    MatMenuModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
