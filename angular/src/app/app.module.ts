import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { TopGeneralFeedComponent } from './top-general-feed/top-general-feed.component';
import { TopTargetedFeedComponent } from './top-targeted-feed/top-targeted-feed.component';
@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    TopGeneralFeedComponent,
    TopTargetedFeedComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
